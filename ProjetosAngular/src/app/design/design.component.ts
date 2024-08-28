import {Component, OnInit} from '@angular/core';
import {BookService} from "../services/livros.service";


@Component({
  selector: 'app-design',
  templateUrl: './design.component.html',
  styleUrl: './design.component.css'
})
export class DesignComponent implements OnInit {
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
