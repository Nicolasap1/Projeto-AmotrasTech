import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule} from "@angular/common/http";
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {UserService} from "./services/item.service";
import {CategoryService} from "./services/category.service";
import { NovaabaComponent } from './novaaba/novaaba.component';
import { UsersComponent } from './users/users.component';
import { LivrosComponent } from './livros/livros.component';
import {BookService} from "./services/livros.service";

@NgModule({
  declarations: [
    AppComponent,
    NovaabaComponent,
    UsersComponent,
    LivrosComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
