import {Component, OnInit} from '@angular/core';
import {CategoryService} from "../services/category.service";

@Component({
  selector: 'app-novaaba',
  templateUrl: './novaaba.component.html',
  styleUrl: './novaaba.component.css'
})
export class NovaabaComponent implements OnInit {
  categorias: any[] = [];
  constructor(private categoryService: CategoryService,
  ) {
  }
  ngOnInit() {
    this.loadCategory();
  }

  loadCategory() {
    this.categoryService.getCategories().subscribe((data) => {
      this.categorias = data;
    });
  }
}
