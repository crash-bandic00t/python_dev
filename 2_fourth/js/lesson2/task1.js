/* Задание 1.
Объясните почему код даёт именно такие результаты?
*/
'use strict'

//пример 1
let a = 1, b = 1, c, d;
c = ++a;
alert(c); // ответ: 2
// Так как ++ это префикс, то сначала "a" увеличится на 1, а потом это число запишется в "с"
// a: 2
// b: 1
// c: 2
// d: undefined

//пример 2
d = b++;
alert(d); //ответ: 1
// Так как ++ это постфикс, то сначала в "d" запишется  "b", а потом "b" увеличится на 1.
// a: 2
// b: 2
// c: 2
// d: 1

//пример 3
c = 2 + ++a;
alert(c); //ответ: 5
// Так как ++ это префикс, то сначала "a" увеличится на 1 и будет равно 3, а потом в "с" запишется результат 2+3.
// a: 3
// b: 2
// c: 5
// d: 1

//пример 4
d = 2 + b++;
alert(d); //ответ: 4
alert(a); //3
alert(b); //3
// Так как ++ это постфикс, то сначала в "d" запишется  2+2, а потом "b" увеличится на 1.
// a: 3
// b: 3
// c: 5
// d: 4