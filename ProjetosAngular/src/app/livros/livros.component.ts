import {Component, OnInit} from '@angular/core';
import {BookService} from "../services/livros.service";

@Component({
  selector: 'app-livros',
  templateUrl: './livros.component.html',
  styleUrl: './livros.component.css'
})
export class LivrosComponent implements OnInit {
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
