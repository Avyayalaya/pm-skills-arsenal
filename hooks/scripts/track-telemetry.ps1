# Local telemetry hook for PM Skills Arsenal (PowerShell variant).
#
# Mirrors track-telemetry.sh. Reads a JSON event from stdin, detects host,
# decides if the event is a pm-skills skill invocation, and appends one line
# to a local JSONL log. No remote network calls.
#
# Modes:
#   - default:  read stdin, emit, exit 0
#   - -Test:    run self-test; exit 0 on pass, 1 on fail

[CmdletBinding()]
param(
    [switch]$Test
)

$ErrorActionPreference = 'SilentlyContinue'

$LogDir = if ($env:PM_SKILLS_TELEMETRY_LOG_DIR) { $env:PM_SKILLS_TELEMETRY_LOG_DIR } else { Join-Path $env:USERPROFILE '.pm-skills-telemetry' }
$LogFile = if ($env:PM_SKILLS_TELEMETRY_LOG) { $env:PM_SKILLS_TELEMETRY_LOG } else { Join-Path $LogDir 'events.jsonl' }

function Detect-Host {
    param([string]$Payload)
    if ($env:COPILOT_CLI -eq '1') { return 'copilot-cli' }
    if ($Payload -match '"toolArgs"' -and $Payload -notmatch '"hook_event_name"') { return 'copilot-cli' }
    if ($Payload -match '"hook_event_name"') {
        if ($Payload -match '__vscode' -or $Payload -match '"transcript_path"[^"]*"[^"]*Code') { return 'vscode' }
        return 'claude-code'
    }
    if ($env:CURSOR_PLUGIN_ROOT) { return 'cursor' }
    return 'unknown'
}

function Is-SkillEvent {
    param([string]$Payload)
    if ($Payload -match '"tool_name"\s*:\s*"Skill"' -or
        $Payload -match '"toolName"\s*:\s*"skill"' -or
        $Payload -match '"tool_name"\s*:\s*"skill"') { return $true }
    if ($Payload -match 'pm-skills' -or $Payload -match 'pm_skills') { return $true }
    if ($Payload -match '/skills/[^/]+/SKILL\.md') { return $true }
    return $false
}

function Extract-SkillName {
    param([string]$Payload)
    $m = [regex]::Match($Payload, '"skill_name"\s*:\s*"([^"]+)"')
    if ($m.Success) { return $m.Groups[1].Value }
    $m = [regex]::Match($Payload, '"name"\s*:\s*"([^"]+)"')
    if ($m.Success) { return $m.Groups[1].Value }
    $m = [regex]::Match($Payload, '/skills/([a-z0-9-]+)/SKILL\.md')
    if ($m.Success) { return $m.Groups[1].Value }
    return 'unknown'
}

function Emit-Line {
    param([string]$Line)
    try {
        if (-not (Test-Path $LogDir)) { New-Item -ItemType Directory -Path $LogDir -Force | Out-Null }
        Add-Content -Path $LogFile -Value $Line -Encoding UTF8
    } catch { }
}

if ($Test) {
    $payload = '{"hook_event_name":"PostToolUse","tool_name":"Skill","tool_input":{"skill_name":"competitive-market-analysis"}}'
    $host_id = Detect-Host -Payload $payload
    if ($host_id -ne 'claude-code') { Write-Error "FAIL: detect_host returned '$host_id' (expected claude-code)"; exit 1 }
    if (-not (Is-SkillEvent -Payload $payload)) { Write-Error 'FAIL: Is-SkillEvent returned false'; exit 1 }
    $name = Extract-SkillName -Payload $payload
    if ($name -ne 'competitive-market-analysis') { Write-Error "FAIL: Extract-SkillName returned '$name'"; exit 1 }
    Write-Output 'PASS: track-telemetry.ps1 self-test'
    exit 0
}

$Payload = ''
try { $Payload = [Console]::In.ReadToEnd() } catch { $Payload = '' }
if ([string]::IsNullOrWhiteSpace($Payload)) { exit 0 }

if (-not (Is-SkillEvent -Payload $Payload)) { exit 0 }

$host_id = Detect-Host -Payload $Payload
$skill = Extract-SkillName -Payload $Payload
$ts = (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')
$line = "{`"ts`":`"$ts`",`"host`":`"$host_id`",`"event`":`"skill_invocation`",`"skill`":`"$skill`",`"plugin`":`"pm-skills`",`"plugin_version`":`"2.1.0`"}"
Emit-Line -Line $line
exit 0
