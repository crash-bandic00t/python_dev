/* Задание 5.
Реализовать функцию с тремя параметрами: function mathOperation(arg1, arg2, operation),
где arg1, arg2 – значения аргументов, operation – строка с названием операции. В зависимости от
переданного значения операции (использовать switch) выполнить одну из арифметических
операций
(использовать функции из задания 4) и вернуть полученное значение.
*/

'use strict'

function mathOperation(arg1, arg2, operation) {
    switch(operation) {
        case '/':
            return arg1 / arg2
      
        case '*':
            return arg1 * arg2

        case '+':
            return arg1 + arg2

        case '-':
            return arg1 - arg2
      }
}

console.log(mathOperation(6, 3, '/'))