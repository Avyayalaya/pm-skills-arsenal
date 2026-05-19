#!/bin/bash
# Local telemetry hook for PM Skills Arsenal.
#
# Purpose: emit one anonymized JSON line per skill invocation to a local log so
# adoption can be measured per-harness without sending data anywhere.
#
# Reads a JSON event from stdin (the host posts the tool-use payload after each
# tool call), detects the host, decides whether this event represents a
# pm-skills skill invocation, and appends one line to the telemetry log.
#
# Hosts handled (detection mirrors microsoft/azure-skills's track-telemetry.sh):
#   - Copilot CLI:   COPILOT_CLI=1, or camelCase fields without `hook_event_name`
#   - Claude Code:   has `hook_event_name`, `tool_use_id` lacks `__vscode`
#   - Cursor:        invoked via cursor-hooks.json (no extra detection needed)
#   - VS Code:       has `hook_event_name`, `tool_use_id` contains `__vscode`
#                    OR `transcript_path` contains "Code"
#
# Modes:
#   - default:       read stdin, emit telemetry line, exit 0
#   - --test:        run a self-test (no stdin); exit 0 on pass, 1 on fail
#
# Output path: $PM_SKILLS_TELEMETRY_LOG (default ~/.pm-skills-telemetry/events.jsonl)
# No external network calls. Local file only.

set -u
LOG_DIR="${PM_SKILLS_TELEMETRY_LOG_DIR:-$HOME/.pm-skills-telemetry}"
LOG_FILE="${PM_SKILLS_TELEMETRY_LOG:-$LOG_DIR/events.jsonl}"

emit_line() {
  # Always succeed; never break the host on telemetry failure.
  mkdir -p "$LOG_DIR" 2>/dev/null || return 0
  printf '%s\n' "$1" >> "$LOG_FILE" 2>/dev/null || return 0
}

iso_now() {
  date -u +"%Y-%m-%dT%H:%M:%SZ" 2>/dev/null || printf 'unknown'
}

detect_host() {
  local payload="$1"
  if [ "${COPILOT_CLI:-0}" = "1" ]; then
    printf 'copilot-cli'
    return
  fi
  case "$payload" in
    *'"toolArgs"'*) [[ "$payload" != *'"hook_event_name"'* ]] && { printf 'copilot-cli'; return; } ;;
  esac
  case "$payload" in
    *'"hook_event_name"'*)
      case "$payload" in
        *'__vscode'*|*'"transcript_path"'*'Code'*) printf 'vscode'; return ;;
        *) printf 'claude-code'; return ;;
      esac
      ;;
  esac
  if [ -n "${CURSOR_PLUGIN_ROOT:-}" ]; then
    printf 'cursor'
    return
  fi
  printf 'unknown'
}

extract_field() {
  # crude grep-based JSON field extraction; good enough for telemetry
  printf '%s' "$1" | sed -n 's/.*"'"$2"'"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -n 1
}

is_skill_event() {
  # Returns 0 if the event looks like a pm-skills skill invocation.
  local payload="$1"
  case "$payload" in
    *'"tool_name"'*'"Skill"'*|*'"toolName"'*'"skill"'*|*'"tool_name"'*'"skill"'*) return 0 ;;
    *'pm-skills'*|*'pm_skills'*) return 0 ;;
    *'/skills/'*'/SKILL.md'*) return 0 ;;
  esac
  return 1
}

extract_skill_name() {
  local payload="$1"
  # try common shapes; bail on unknown
  local skill
  skill=$(printf '%s' "$payload" | sed -n 's/.*"skill_name"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -n 1)
  [ -z "$skill" ] && skill=$(printf '%s' "$payload" | sed -n 's/.*"name"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -n 1)
  [ -z "$skill" ] && skill=$(printf '%s' "$payload" | sed -n 's|.*/skills/\([a-z0-9-]*\)/SKILL\.md.*|\1|p' | head -n 1)
  [ -z "$skill" ] && skill='unknown'
  printf '%s' "$skill"
}

run_test() {
  local payload='{"hook_event_name":"PostToolUse","tool_name":"Skill","tool_input":{"skill_name":"competitive-market-analysis"}}'
  local host
  host=$(detect_host "$payload")
  if [ "$host" != "claude-code" ]; then
    echo "FAIL: detect_host returned '$host' (expected claude-code)" >&2
    exit 1
  fi
  if ! is_skill_event "$payload"; then
    echo "FAIL: is_skill_event returned false for a known skill payload" >&2
    exit 1
  fi
  local name
  name=$(extract_skill_name "$payload")
  if [ "$name" != "competitive-market-analysis" ]; then
    echo "FAIL: extract_skill_name returned '$name' (expected competitive-market-analysis)" >&2
    exit 1
  fi
  echo "PASS: track-telemetry.sh self-test"
  exit 0
}

if [ "${1:-}" = "--test" ]; then
  run_test
fi

# stdin path: read once, decide, emit
PAYLOAD="$(cat 2>/dev/null || true)"
[ -z "$PAYLOAD" ] && exit 0

if ! is_skill_event "$PAYLOAD"; then
  exit 0
fi

HOST=$(detect_host "$PAYLOAD")
SKILL=$(extract_skill_name "$PAYLOAD")
TS=$(iso_now)
LINE=$(printf '{"ts":"%s","host":"%s","event":"skill_invocation","skill":"%s","plugin":"pm-skills","plugin_version":"2.1.0"}' "$TS" "$HOST" "$SKILL")
emit_line "$LINE"
exit 0
