

let operators_list = ["add", "subtract", "multiply", "divide"]

let number1 = 10
let number2 = 15


 funciton calculate (number1, number2, operator) {

    switch (operator) {

        case "add" : {
            
            return number1 + number2;
        }
    
        case "subtract" : {
    
            return number1 - number2;
        }
    
        case "multiply" : {
    
            return number1 * number2;
        }
    
        case "divide" : {
            if number2 === 0 {
                return  "cannot divide by zero;"
            }
            else {
            return number1 / number2;
            }
        }

    }

}


    







