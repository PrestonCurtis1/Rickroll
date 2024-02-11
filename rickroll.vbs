Set objPlayer = CreateObject("WMPlayer.OCX")
objPlayer.URL = "rick.mp3"
objPlayer.settings.setMode "loop", true
objPlayer.controls.play

Do
  WScript.Sleep 100
  Set objShell = CreateObject("WScript.Shell")
  objShell.SendKeys(chr(&hAF))
  If objPlayer.playState = 1 Then ' 1 means it's stopped
    objPlayer.controls.play
  End If
Loop