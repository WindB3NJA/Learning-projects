//Jugador
let playerAtack 
let playerBattleLife = 3 ;
//Rival
let rivalAtack
let rivalBattleLife = 3 ;
//se Incializa el JavaScript con una funcion que espera al usuario que apriente una opcion para disparar el juego
function gameLoading() {
    //Mostrar las secciones del juego
    let displayChoiseAtack = document.getElementById("player-atack-choise")
    displayChoiseAtack.style.display = "none"
    let displayBattleMessages = document.getElementById("battle-messages")
    displayBattleMessages.style.display = "none"
    let displayBattleResults = document.getElementById("battle-Results")
    displayBattleResults.style.display = "none"
    let displayRestart = document.getElementById("button-restart")
    displayRestart.style.display = "none"
    //Boton para verificar si el usuario al haber tocado ya click en mokepon y al boton de confirmar seleccione el mokepon
    let buttonSelectMokepon = document.getElementById("button-select-mokepon") ;
    buttonSelectMokepon.addEventListener("click", PlayerChoise)
    //Botones de seleccion de ataque
    let playerButtonFire = document.getElementById("button-fire") ;
    playerButtonFire.addEventListener("click", PlayerButtonFire)
    let playerButtonWater = document.getElementById("button-water") ;
    playerButtonWater.addEventListener("click", PlayerButtonWater)
    let playerButtonPlant = document.getElementById("button-plant") ;
    playerButtonPlant.addEventListener("click", PlayerButtonPlant)
    //Reiniciar el juego
    let gameButtonRestart = document.getElementById("button-restart")
    gameButtonRestart.addEventListener("click", gameRestart)
}
//Funcion para reiniciar el juego
function gameRestart() {
    location.reload()
}
//Generador de numeros aleatorios
function num_random(min,max) {
    return Math.floor(Math.random()*(max-min+1)+min)
}
//Selecion del jugaro a la criatura llamada mokepon
function PlayerChoise() {
    //Imagenes de los mokepones
    let PlayerMokeponImage = document.createElement("img");
    //elecion del Mokepon
    let choiseRaditen = document.getElementById("Radinten") ;
    let choiseMizutana = document.getElementById("Mizutana") ;
    let choiseHanize = document.getElementById("Hanize") ;
    let choiseMizuhi = document.getElementById("Mizuhi") ;
    let choiseHazu = document.getElementById("Hazu") ;
    let choiseHanine = document.getElementById("Hahine") ;
    let PlayerMokepon = document.getElementById("player-mokepon-name") ;

    if (choiseRaditen.checked) {
        PlayerMokepon.innerHTML = "🔥Raditen"
        alert("Haz seleccionado a 🔥Raditen")
        PlayerMokeponImage.src ="content/assets/Mokepons/Radinten.png"
        document.getElementById("image-player-mokepon").appendChild(PlayerMokeponImage);
    } else if (choiseMizutana.checked) {
        PlayerMokepon.innerHTML = "💧Mizutana"
        alert("Haz seleccionado a 💧Mizutana")
        PlayerMokeponImage.src ="content/assets/Mokepons/Mizutana.png"
        document.getElementById("image-player-mokepon").appendChild(PlayerMokeponImage);
    } else if (choiseHanize.checked) {
        PlayerMokepon.innerHTML = "🌱Hanize"
        alert("Haz seleccionado a 🌱Hanize")
        PlayerMokeponImage.src ="content/assets/Mokepons/Hanize.png"
        document.getElementById("image-player-mokepon").appendChild(PlayerMokeponImage);
    } else if (choiseMizuhi.checked) {
        PlayerMokepon.innerHTML = "🔥💧Mizuhi"
        alert("Haz seleccionado a 🔥💧Mizuhi")
        PlayerMokeponImage.src ="content/assets/Mokepons/Mizuhi.png"
        document.getElementById("image-player-mokepon").appendChild(PlayerMokeponImage);
    } else if (choiseHazu.checked) {
        PlayerMokepon.innerHTML = "💧🌱Hazu"
        alert("Haz seleccionado a 💧🌱Hazu")
        PlayerMokeponImage.src ="content/assets/Mokepons/Hazu.png"
        document.getElementById("image-player-mokepon").appendChild(PlayerMokeponImage);
    } else if (choiseHanine.checked) {
        PlayerMokepon.innerHTML = "🌱🔥Hahine"
        alert("Haz seleccionado a 🌱🔥Hahine")
        PlayerMokeponImage.src ="content/assets/Mokepons/Hahine.png"
        document.getElementById("image-player-mokepon").appendChild(PlayerMokeponImage);
    } else {
        alert("Seleccione un Mokepon Porfavor")
        gameRestart()
    }
    //Mostrar en pantalla la siguiente seccion
    let displayPlayerChoise = document.getElementById("player-Mokepon-choise")
    displayPlayerChoise.style.display = "none"
    let displayChoiseAtack = document.getElementById("player-atack-choise")
    displayChoiseAtack.style.display = "block"
    let displayBattleMessages = document.getElementById("battle-messages")
    displayBattleMessages.style.display = "block"
    //Eleccion de el rival
    rivalMokeponChoise()
}
//Desicion de la maquina para elegir que a la criatura mokepon que utliza se ejecuta despues de 
function rivalMokeponChoise() {
    let RivalMokeponImage = document.createElement("img");
    let rivalMokeponChoise = num_random(1,6) ;
    let RivalMokepon = document.getElementById("rival-mokepon-name") ;

    if (rivalMokeponChoise == 1) {
        RivalMokepon.innerHTML = "🔥Raditen"
        alert("Tú rival ha seleccionado a 🔥Raditen")
        RivalMokeponImage.src ="content/assets/Mokepons/Radinten.png"
        document.getElementById("image-rival-mokepon").appendChild(RivalMokeponImage);
    } else if (rivalMokeponChoise == 2) {
        RivalMokepon.innerHTML = "💧Mizutana"
        alert("Tú rival ha seleccionado a 💧Mizutana")
        RivalMokeponImage.src ="content/assets/Mokepons/Mizutana.png"
        document.getElementById("image-rival-mokepon").appendChild(RivalMokeponImage);
    } else if (rivalMokeponChoise == 3) {
        RivalMokepon.innerHTML = "🌱Hanize"
        alert("Tú rival ha seleccionado a 🌱Hanize")
        RivalMokeponImage.src ="content/assets/Mokepons/Hanize.png"
        document.getElementById("image-rival-mokepon").appendChild(RivalMokeponImage);
    } else if (rivalMokeponChoise == 4) {
        RivalMokepon.innerHTML = "🔥💧Mizuhi"
        alert("Tú rival ha seleccionado a 🔥💧Mizuhi")
        RivalMokeponImage.src ="content/assets/Mokepons/Mizuhi.png"
        document.getElementById("image-rival-mokepon").appendChild(RivalMokeponImage);
    } else if (rivalMokeponChoise == 5) {
        RivalMokepon.innerHTML = "💧🌱Hazu"
        alert("Tú rival ha seleccionado a 💧🌱Hazu")
        RivalMokeponImage.src ="content/assets/Mokepons/Hazu.png"
        document.getElementById("image-rival-mokepon").appendChild(RivalMokeponImage);
    } else if (rivalMokeponChoise == 6) {
        RivalMokepon.innerHTML = "🌱🔥Hahine"
        alert("Tú rival ha seleccionado a 🌱🔥Hahine")
        RivalMokeponImage.src ="content/assets/Mokepons/Hahine.png"
        document.getElementById("image-rival-mokepon").appendChild(RivalMokeponImage);
    }
}
//Botones de ataque del jugador
//Boton de fuego
function PlayerButtonFire() {
    playerAtack = "Fuego 🔥"
    rivalAtackChoise()
}
//Boton de agua
function PlayerButtonWater() {
    playerAtack = "Agua 💧"
    rivalAtackChoise()
}
//Boton de planta
function PlayerButtonPlant() {
    playerAtack = "Planta 🌱"
    rivalAtackChoise()
}
//Ataque del rival
function rivalAtackChoise() {
    rivalAtackRandomChoise = num_random(1,3) ;
    
    if (rivalAtackRandomChoise == 1){
        rivalAtack = "Fuego 🔥"
    } else if (rivalAtackRandomChoise == 2){
        rivalAtack = "Agua 💧"
    } else if (rivalAtackRandomChoise == 3){
        rivalAtack = "Planta 🌱"
    }
    gameMesaggeStatus()
}
//generador de mensajes de la batalla
function gameMesaggeStatus() {
    let gameBattleResults = "" 
    if (playerAtack == rivalAtack) {
        gameBattleResults = "¡Un empate de Elementos! 😲"
    } else if (playerAtack == "Fuego 🔥" && rivalAtack == "Agua 💧") {
        gameBattleResults = "Te han apagado 😰, ¡Haz Perdido esta ronda!"
        playerBattleLife--
    } else if (playerAtack == "Agua 💧" && rivalAtack == "Planta 🌱") {
        gameBattleResults = "Te han absorido para sus nutrientes 🚱, ¡Haz Perdido esta ronda!"
        playerBattleLife--
    } else if (playerAtack == "Planta 🌱" && rivalAtack == "Fuego 🔥") {
        gameBattleResults = "Te han chamuscado 🥵, ¡Haz Perdido esta ronda!"
        playerBattleLife--
    } else if (playerAtack == "Agua 💧" && rivalAtack == "Fuego 🔥") {
        gameBattleResults = "Apagaste el incendio 💦, ¡Haz Ganado esta ronda!"
        rivalBattleLife--
    } else if (playerAtack == "Planta 🌱" && rivalAtack == "Agua 💧") {
        gameBattleResults = "Que sediento estabas 🤤, ¡Haz Ganado esta ronda!"
        rivalBattleLife--
    } else if (playerAtack == "Fuego 🔥" && rivalAtack == "Planta 🌱") {
        gameBattleResults = "Leña para el asado 🔥, ¡Haz Ganado esta ronda!"
        rivalBattleLife--
    } 
    //Señalar donde se pondra el texto 
    let gameMessageRival  = document.getElementById("Rival-atacks");
    let gameMessageAtack  = document.getElementById("battle-status");
    let gameMessagePlayer = document.getElementById("Player-atacks");
    //En que elemento se guardara
    let MessageRival = document.createElement("p");
    let BattleStatus = document.createElement("p");
    let MessagePlayer = document.createElement("p");
    //Guardar los textos que insertara
    MessageRival.innerHTML = rivalAtack
    BattleStatus.innerHTML = gameBattleResults
    MessagePlayer.innerHTML = playerAtack
    //Insertar el elemento en el HTML
    gameMessageRival.appendChild(MessageRival);
    gameMessageAtack.appendChild(BattleStatus);
    gameMessagePlayer.appendChild(MessagePlayer);
    //Sistema de vidas en HTML
    let playerStringLife = document.getElementById("player-life");
    let rivalStringLife = document.getElementById("rival-life");
    //Comparador de vidas y mensajes
    if(playerBattleLife == 0 || rivalBattleLife == 0) {
        let displayBattleResults = document.getElementById("battle-Results")
        displayBattleResults.style.display = "block"
        let displayRestart = document.getElementById("button-restart")
        displayRestart.style.display = "block"
        playerStringLife.innerHTML = playerBattleLife
        rivalStringLife.innerHTML = rivalBattleLife
        gameBattleFinalResults()
    } else {
        playerStringLife.innerHTML = playerBattleLife
        rivalStringLife.innerHTML = rivalBattleLife
    }

}
//Desactivador de botones de ataque
function buttonDisableAtack() {
    let playerButtonFire = document.getElementById("button-fire") ;
    playerButtonFire.disabled = true
    let playerButtonWater = document.getElementById("button-water") ;
    playerButtonWater.disabled = true
    let playerButtonPlant = document.getElementById("button-plant") ;
    playerButtonPlant.disabled = true
}
//Comparador de vidas 
function gameBattleFinalResults() {
    let BattleResults  = document.getElementById("battle-Results");
    let BattleResultsString = document.createElement("p");
    if (playerBattleLife == 0){
        //Perdiste
        buttonDisableAtack()
        BattleResultsString.innerHTML = "😞Haz Perdido la Batalla😞, con " + playerBattleLife + " Puntos vitales vs los Puntos "+ rivalBattleLife +" vitales del enemigo"
        //Imagen del personaje rival 
        BattleResults.appendChild(BattleResultsString);
    } else if (rivalBattleLife == 0){
        //ganaste
        buttonDisableAtack()
        BattleResultsString.innerHTML = "🎊Haz Ganado la Batalla🎊, con " + playerBattleLife + " Puntos vitales vs los Puntos "+ rivalBattleLife +" vitales del enemigo"
        //IMAGEN del personaje del jugador
        BattleResults.appendChild(BattleResultsString);
    }
}

//Se espera a que la pagina carge para luego correr el JavaScript
window.addEventListener("load", gameLoading)