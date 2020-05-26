function dynamicdropdown(listindex)
  {
    // alert(direction.options[direction.selectedIndex].text);
    switch (listindex)
    {
      case "DAAF" :
        document.getElementById("id_informations").options[1]=new Option("Transfert de référence individuelle sans foncier","Transfert de référence individuelle sans foncier");
        break;
    }
    return true;
  }