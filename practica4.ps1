function Show-Menu
{
     param (
       [string]$Title = 'Menu'
     )
     cls
     Write-Host "================ $Title ================"
    
     Write-Host "1: Presione '1' ver teams."
     Write-Host "2: Presione '2' crear teams "
     Write-Host "3: Presione '3' eliminar teams"
     Write-Host "4: Presione '4' cambiar imagen de teams"
     Write-Host "5: Presione '5' agregar a teams"
     Write-Host "Q: Presione 'Q' para salir."
}
$correo = Connect-MicrosoftTeams
$correo = $correo.Account

do
{
     Show-Menu
     $input = Read-Host "Seleccione una opcion"
     switch ($input)
     {
           '1' {
                cls
                Get-Team -User ${correo}
                
           } '2' {
                cls
                $team_name = Read-Host "Nombre de tu nuevo team"
                $team_description = Read-Host "Escribe la descripcion de tu nuevo team"
                $visibility = Read-Host "Escribe si quieres que sea privado o publico, solo debe ser Public or Private"
                New-Team -DisplayName "$team_name" -Description "$team_description" -Visibility "$visibility"
           } '3' {
                cls
                Get-Team -User ${correo}
                $idequipo = Read-Host "Escriba el ID del equipo que desea eliminar"
                Remove-Team -GroupId ${idequipo}
           } '4' {
                cls
                $teamid = Read-Host "Escriba el group id"
                $pic = Read-Host "Escriba la direccion de la imagen"
                Set-TeamPicture -GroupID ${teamid} -ImagePath ${pic}
           } '5' {
                cls
                $teamid = Read-Host "Escriba el group id"
                $usuario = Read-Host "Escriba el correo del usuario que desea agregar"
                Add-TeamUser -GroupId ${teamid} -User ${usuario}
                
                
           } 'q' {
                return
           }
     }
     pause
}
until ($input -eq 'q')
