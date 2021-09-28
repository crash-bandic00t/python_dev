/* (Это задание не является частью курса, можете его не делать, оно для тех кому мало
обычных заданий, требует времени и возможно гугления, делайте по желанию.)
Программа должна спросить у пользователя число, это будет количество денег, которое он хочет
положить на счет в банке. Затем программа должна выдать примерно такое сообщение:
"Ваша сумма в 101 рубль успешно зачислена." - в случае если пользователь ввел 101.
"Ваша сумма в 10020 рублей успешно зачислена." - в случае если пользователь ввел 10020.
"Ваша сумма в 120104 рубля успешно зачислена." - в случае если пользователь ввел 120104.
То есть ваша задача выводить слово «рубль» в правильном падеже, в зависимости от введенного
числа.
*/

'use strict'

function moneyInfo(money, word) {
    alert(`Ваша сумма в ${money} ${word} успешно зачислена.`)
}
let money = parseInt(prompt('Введите зачисляемую сумму:'))
if (!isNaN(money)) {
    let lastNubmer = money % 10
    let lastTwoNubmers = money % 100
    if (lastTwoNubmers % 100 == 11 ||
        lastTwoNubmers % 100 == 12 ||
        lastTwoNubmers % 100 == 13 ||
        lastTwoNubmers % 100 == 14
        ) {
        moneyInfo(money, 'рублей')
    } else if (lastNubmer == 1) {
        moneyInfo(money, 'рубль')
    } else if (
        lastNubmer == 0 ||
        lastNubmer == 5 ||
        lastNubmer == 6 ||
        lastNubmer == 7 ||
        lastNubmer == 8 ||
        lastNubmer == 9) {
        moneyInfo(money, 'рублей')   
    } else if (
        lastNubmer == 2 ||
        lastNubmer == 3 ||
        lastNubmer == 4) {
        moneyInfo(money, 'рубля')
        }1
} else {
    alert('Введите число!')
}