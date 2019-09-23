entradas = list(input().split())

typeof = {
    "tesoura": {
        "papel":"Bazinga!", 
        "lagarto":"Bazinga!", 
        "pedra":"Raj trapaceou!",   
        "tesoura":"De novo!", 
        "Spock":"Raj trapaceou!"
    },
    "papel": {
        "tesoura":"Raj trapaceou!",
        "papel":"De novo!",
        "lagarto":"Raj trapaceou!",
        "pedra":"Bazinga!",
        "Spock":"Bazinga!",
    },
    "lagarto": {
        "tesoura":"Raj trapaceou!",
        "papel":"Bazinga!",
        "lagarto":"De novo!",
        "pedra":"Raj trapaceou!",
        "Spock":"Bazinga!"
    },
    "pedra": {
        "tesoura":"Bazinga!",
        "papel":"Raj trapaceou!",
        "lagarto":"Bazinga!",
        "pedra":"De novo!",
        "Spock":"Raj trapaceou!"
    },
    "Spock": {
        "tesoura":"Bazinga!",
        "papel":"Raj trapaceou!",
        "lagarto":"Raj trapaceou!",
        "pedra":"Bazinga!",
        "Spock":"De novo!"
    }
}
    
print(typeof[entradas[0]][entradas[1]])
