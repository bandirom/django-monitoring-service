
if(typeof open_menu !== "undefined")
{
    $open =  $('#'+ open_menu)
    $open.addClass('menu-open')
}

if(typeof active_menu !== "undefined")
{
    $menu =  $('#'+ active_menu)
    $menu.addClass('active')
}
if(typeof active_submenu !== "undefined")
{
    $submenu = $('#'+ active_submenu)
    $submenu.addClass('active')
}
