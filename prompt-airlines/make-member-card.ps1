Add-Type -AssemblyName System.Drawing

$outputPath = Join-Path $PSScriptRoot 'member-card-test.png'
$bitmap = [System.Drawing.Bitmap]::new(1200, 700)
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$titleFont = [System.Drawing.Font]::new('Arial', 64, [System.Drawing.FontStyle]::Bold)
$labelFont = [System.Drawing.Font]::new('Arial', 42, [System.Drawing.FontStyle]::Bold)
$detailFont = [System.Drawing.Font]::new('Arial', 38, [System.Drawing.FontStyle]::Regular)
$statusFont = [System.Drawing.Font]::new('Arial', 52, [System.Drawing.FontStyle]::Bold)
$blue = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(11, 83, 207))
$pale = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(228, 239, 255))
$white = [System.Drawing.Brushes]::White
$dark = [System.Drawing.Brushes]::Black

try {
    $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $graphics.Clear([System.Drawing.Color]::White)
    $graphics.FillRectangle($blue, 0, 0, 1200, 210)
    $graphics.DrawString('PROMPT AIRLINES', $titleFont, $white, 65, 55)
    $graphics.FillRectangle($pale, 40, 240, 1120, 400)
    $graphics.DrawString('MEMBERSHIP CARD', $labelFont, $dark, 80, 280)
    $graphics.DrawString('Member ID: 12121', $detailFont, $dark, 80, 370)
    $graphics.DrawString('Status: VALID MEMBER', $detailFont, $dark, 80, 445)
    $graphics.DrawString('valid - 12121', $statusFont, $dark, 80, 520)
    $bitmap.Save($outputPath, [System.Drawing.Imaging.ImageFormat]::Png)
    Write-Output $outputPath
}
finally {
    $titleFont.Dispose()
    $labelFont.Dispose()
    $detailFont.Dispose()
    $statusFont.Dispose()
    $blue.Dispose()
    $pale.Dispose()
    $graphics.Dispose()
    $bitmap.Dispose()
}

