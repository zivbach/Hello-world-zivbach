function updateDate(){
    var d = new Date();
    var a = d.getMonth();
    var months = []
    var m = ["Januari", "Feruar", "March", "april","may","jun","july","augost","sep","oct","nov","December"]
    document.getElementById("imgDate").innerHTML=m[d.getMonth()] +" "+ d.getFullYear();
        }