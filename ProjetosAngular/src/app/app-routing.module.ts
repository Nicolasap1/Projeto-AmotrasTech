import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import {NovaabaComponent} from "./novaaba/novaaba.component";
import {UsersComponent} from "./users/users.component";
import {LivrosComponent} from "./livros/livros.component";
import {MenuComponent} from "./menu/menu.component";

const routes: Routes = [
  { path: 'users', component: UsersComponent },
  { path: 'categories', component: NovaabaComponent },
  { path: 'livros', component: LivrosComponent },
  { path: 'menu', component: MenuComponent },
 ];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
