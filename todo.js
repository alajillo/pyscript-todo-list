class TodoList{
    constructor(parentElement){
        this.parentElement = parentElement;
        this.currentId = 0;
        this.initInput();
        this.initButton();
        this.inputList();
    }
    initButton(){
        this.buttonElement = document.createElement('button');
        this.buttonElement.innerText = "add todo";
        this.parentElement.append(this.buttonElement);
        this.buttonElement.addEventListener("click",this.addTodo.bind(this));
    }
    initInput(){
        this.inputElement = document.createElement('input');
        this.parentElement.append(this.inputElement);
    }
    inputList(){
        this.listElement = document.createElement('ul');
        this.parentElement.append(this.listElement);
    }
    addTodo(){
        const text = this.inputElement.value;
        const newItem = new Item(text,this.currentId);
        this.currentId = this.currentId + 1;
        newItem.onRemove(this.removeTodo.bind(this));
        this.listElement.append(newItem.item);
    }
    removeTodo(event){
        const targetElement = event.target.closest('li');
        this.listElement.removeChild(targetElement);
    }
}

class Item{
    constructor(text,id){
        this.item = document.createElement('li');
        this.item.setAttribute('data-id',id);
        this.item.innerText = text;
        this.removeButton = document.createElement('button');
        this.removeButton.innerText = 'remove';
        this.item.append(this.removeButton);
    }
    onRemove(cb){
        this.removeButton.addEventListener('click',cb);
    }
}
const app = document.getElementById('app');

new TodoList(app);