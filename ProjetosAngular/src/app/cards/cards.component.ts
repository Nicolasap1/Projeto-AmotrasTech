import {Component, OnInit} from '@angular/core';
import {BookService} from "../services/livros.service";

@Component({
  selector: 'app-cards',
  templateUrl: './cards.component.html',
  styleUrl: './cards.component.css'
})
export class CardsComponent implements OnInit {
  livro: any[] = [];
  constructor(private bookService: BookService,
  ) {
  }
  ngOnInit() {
    this.loadBooks();
  }

  loadBooks() {
    this.bookService.getBooks().subscribe((data) => {
      this.livro = data;
    });
  }
}
