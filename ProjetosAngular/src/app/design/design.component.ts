import {Component, OnInit} from '@angular/core';
import {BookService} from "../services/livros.service";


@Component({
  selector: 'app-design',
  templateUrl: './design.component.html',
  styleUrl: './design.component.css'
})
export class DesignComponent implements OnInit {
  livro: any[] = [];
  livro1:any;
  livro2:any;
  constructor(private bookService: BookService,
  ) { }
  ngOnInit() {
    this.loadBooks();
  }

  loadBooks() {
    this.bookService.getBooks().subscribe((data) => {
      this.livro = data;
    });

    this.bookService.getBook(3).subscribe(data => {
      this.livro1 = data;
    });
    this.bookService.getBook(4).subscribe(data => {
      this.livro2 = data;
    });
  }
}
