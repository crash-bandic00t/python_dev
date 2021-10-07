/* Задание 4.
Перед вами находится массив с продуктами в интернет-магазине. Вам нужно:
1. Получить все товары, у которых есть фотографии
2.  Отсортируйте товары по цене (от низкой цены к высокой)
*/
'use strict'

const products = [
    {
        id: 3,
        price: 127,
        photos: [
            "1.jpg",
            "2.jpg",
        ]
    },
    {
        id: 5,
        price: 499,
        photos: []
    },
    {
        id: 10,
        price: 26,
        photos: [
            "3.jpg"
        ]
    },
    {
        id: 8,
        price: 78,
    },
];
const result1 = products.filter(function(e) { // Получить все товары, у которых есть фотографии
    if (e.photos && e.photos.length > 0) {
        return true
    }
})
console.log(result1)

const result2 = products.sort(function (a, b) {
    return a.price - b.price
})
console.log(result2)