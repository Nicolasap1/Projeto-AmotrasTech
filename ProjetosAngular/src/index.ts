class App{
    private readonly message: string;
    constructor(message: string) {
      this.message = message;
    }
    public show(elementId: string): void{
        const element = document.getElementById(elementId);
        if (element){
            element.innerText = this.message
        }
    }
}
const app = new App('Óla, Typescript!');
app.show("message");
