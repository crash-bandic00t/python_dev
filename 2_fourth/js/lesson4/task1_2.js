/* Задание 1.2
Сделайте в стиле es5, а затем в стиле es6 (по аналогии из дополнительных
видео -> 3 примеры наследования -> механика наследования),
а) конструктор Post, который принимает параметры author, text, date и сохраняет их как свойства объекта. Объекты
типа Post должны иметь метод edit, который будет принимать текст и записывать его в свойство text объекта.
б) конструктор AttachedPost, который принимает параметры author, text, date. Проинициализируйте эти свойства с
помощью конструктора Post, чтобы не дублировать код. Также в конструкторе AttachedPost должно создаваться
свойство highlighted со значением false. Унаследуйте в объектах типа AttachedPost методы из Post.
Объекты типа AttachedPost должны иметь метод makeTextHighlighted, который будет назначать свойству
highlighted значение true.
*/

'use strict'

// ES 5

function Post(author, text, date) {
    this.author = author;
    this.text = text;
    this.date = date;
}

Post.prototype.edit = function(newText) {
    this.text = newText
};

function AttachedPost(author, text, date) {
    Post.call(this, author, text, date);
    this.highlighted = false;
}

AttachedPost.prototype = Object.create(Post.prototype);
AttachedPost.prototype.constructor = AttachedPost;

AttachedPost.prototype.makeTextHighlighted = function() {
    this.highlighted = true;
};

let post1 = new Post('Sasha', 'text1', '07.10.2021');
let post2 = new AttachedPost('Masha', 'text2', '15.09.2020');
post2.makeTextHighlighted();

// ES 6

class Post2 {
    constructor(author, text, date) {
        this.author = author;
        this.text = text;
        this.date = date;
    }

    edit(newText) {
        this.text = newText
    }
}

let post3 = new Post2('John', 'text3', '10.08.2015')
post3.edit('Новый текст')
console.log(post3.text)

class AttachedPost2 extends Post2 {
    constructor(author, text, date) {
        super(author, text, date);
        this.highlighted = false;
    }

    makeTextHighlighted() {
        this.highlighted = true;
    }
}
let post4 = new AttachedPost2('Olivia', 'text4', '23.02.2022')
console.log(post4.highlighted)
post4.makeTextHighlighted();
console.log(post4.highlighted)
