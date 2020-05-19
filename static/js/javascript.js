var kastKlassigaElemendid = document.getElementsByClassName("kast");

var muudaMitmeSisestatudNumbriFonti = function() {
  this.style.fontSize = "0.8em";
  this.style.paddingBottom = "22px";
  this.style.paddingLeft = "1px";
  this.style.textAlign = "left";
};

var muudaMitmeSisestatudNumbriFonti2 = function() {
  if (this.value.length > 1) {
    this.style.fontSize = "0.8em";
    this.style.paddingBottom = "0px";
    this.style.paddingLeft = "0px";
    this.style.textAlign = "center";
  }
  if (this.value.length == 1) {
    this.style.fontSize = "2em";
    this.style.paddingBottom = "0px";
    this.style.paddingLeft = "0px";
    this.style.textAlign = "center";
  }
};

for (var i = 0; i < kastKlassigaElemendid.length; i++) {
  kastKlassigaElemendid[i].addEventListener('input', muudaMitmeSisestatudNumbriFonti2);
}

var vahetaChecki = function(key) {
  if (key.keyCode === 9) {
    key.preventDefault();
    var fookusesKast = document.activeElement;
    if (fookusesKast.localName == "body") return;
    if (document.getElementById("teine").checked == true) {
      document.getElementById("esimene").checked = true;
      fookusesKast.style.paddingBottom = "0px";
      fookusesKast.style.paddingLeft = "1px";
      fookusesKast.style.textAlign = "center";
      if (fookusesKast.value.length == 1) {
        fookusesKast.style.fontSize = "2em";
      }
      for (var i = 0; i < kastKlassigaElemendid.length; i++) {
        kastKlassigaElemendid[i].removeEventListener('input', muudaMitmeSisestatudNumbriFonti);
        kastKlassigaElemendid[i].addEventListener('input', muudaMitmeSisestatudNumbriFonti2);
      }
    }
    else {
      document.getElementById("teine").checked = true;
        fookusesKast.style.paddingBottom = "22px";
        fookusesKast.style.paddingLeft = "1px";
        fookusesKast.style.textAlign = "left";
        fookusesKast.style.fontSize = "0.8em";
      for (var i = 0; i < kastKlassigaElemendid.length; i++) {
        kastKlassigaElemendid[i].removeEventListener('input', muudaMitmeSisestatudNumbriFonti2);
        kastKlassigaElemendid[i].addEventListener('input', muudaMitmeSisestatudNumbriFonti);
      }
    }
  }
};
document.addEventListener('keydown', vahetaChecki);

var teeFookusesKastTühjaks = function(key) {
  if (key.keyCode === 27) {
    document.activeElement.value = "";
  }
};

document.addEventListener('keydown', teeFookusesKastTühjaks);


// ajanäit
var minutid = 0;
var sekundid = 0;

var muudaAega = function() {
  sekundid += 1;
  if (sekundid == 60) {
    minutid += 1;
    sekundid = 0;
    document.getElementById("minutid").innerHTML = (minutid ? (minutid > 9 ? minutid : "0" + minutid) : "00");
    document.getElementById("sekundid").innerHTML = "00";
  }
  else {
    document.getElementById("sekundid").innerHTML = (sekundid ? (sekundid > 9 ? sekundid : "0" + sekundid) : "00");
  }
  
  setTimeout(muudaAega, 1000);
}

muudaAega();

// lõpptulemuse kontrollimine
var tulemuseKontroll = function() {
    var korras = true;
    var koht;
    var tulemuseMassiiv = [];
    for (koht = 0; koht < 81; koht++) {
        tulemuseMassiiv.push(document.getElementsByClassName("kast")[koht].value);
    }
    var ridadeMassiiv = [];
    var reaNumber;
    for (reaNumber = 0; reaNumber < 9; reaNumber++) {
        ridadeMassiiv[reaNumber] = tulemuseMassiiv.slice(reaNumber * 9, reaNumber * 9 + 9);
    }

    //ridade kontroll
    var rida;
    var number;
    ridadeMassiiv.every(rida => {
        if (korras == false) {return false;}
        for (number = 1; number <= 9; number++) {
            if (!rida.includes(number.toString())) {
                korras = false;
                return false;
            }
        }
        return true;
    })

    // kolmeste kastide loomine
    var kolmesteKastideMassiiv = [];
    for (koht = 0; koht < 9; koht ++) {kolmesteKastideMassiiv[koht] = [];}
    var reaNumber;
    for (reaNumber = 0; reaNumber < 9; reaNumber++) {
        for (koht = 0; koht < 9; koht++) {
            kolmesteKastideMassiiv[3 * Math.floor(reaNumber / 3) + Math.floor(koht / 3)].push(ridadeMassiiv[reaNumber][koht]);
        }
    }
    // kolmeste kastide kontroll
    var kast;
    kolmesteKastideMassiiv.every(kast => {
        if (korras == false) {return false;}
        for (number = 1; number <= 9; number++) {
            if (!kast.includes(number.toString())) {
                korras = false;
                return false;
            }
        }
        return true;
    })


    if (korras) return true;
}

var tulemuseSubmit = function() {
  if (!tulemuseKontroll()) {
    alert("Noups");
    return;
  }

  var lahendamisAeg = minutid * 60 + sekundid;
  document.getElementById("lahendamisAeg").value = lahendamisAeg;
  
  document.getElementById("lahendajaNimi").value = prompt("Sisesta edetabeli jaoks oma nimi:")

  document.getElementById("tulemuseSubmit").submit();
}

var muudaTausta = function(selectElement) {
  if (selectElement.value == "Valge") document.body.style.backgroundImage = "none";
  else {
    var pildiURL = "../static/images/background/" + selectElement.value + ".png";
    document.body.style.backgroundImage = "url(" + pildiURL + ")";
  }
}

var muudaMuinasjuttu = function(selectElement) {
  var muinasjuttSourceElement = document.getElementById("muinasjuttSource");

  var muinasjuttURL = "https://tigu.hk.tlu.ee/~silver.abel/Sudoku/" + selectElement.value + ".mp3";
  muinasjuttSourceElement.src = muinasjuttURL;

  document.getElementById("muinasjuttAudio").load();
  document.getElementById("muinasjuttAudio").play();
}

var vahetaLaulu = function() {
  var taustamuusikaSourceElement = document.getElementById("taustamuusikaSource");
  var laulunumber = Number(taustamuusikaSourceElement.src.charAt(taustamuusikaSourceElement.src.length - 5));
  if (laulunumber == 5) laulunumber = 1;
  else laulunumber += 1;
  var taustamuusikaURL = "../static/sounds/music/" + laulunumber + ".mp3";
  taustamuusikaSourceElement.src = taustamuusikaURL;
  document.getElementById("taustamuusikaAudio").load();
  document.getElementById("taustamuusikaAudio").play();
}