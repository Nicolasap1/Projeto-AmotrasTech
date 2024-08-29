import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import {NovaabaComponent} from "./novaaba/novaaba.component";
import {UsersComponent} from "./users/users.component";
import {LivrosComponent} from "./livros/livros.component";
import {LoginComponent} from "./login/login.component";
import {DesignComponent} from "./design/design.component";
import {FooterComponent} from "./footer/footer.component";


const routes: Routes = [
  { path: 'users', component: UsersComponent },
  { path: 'categories', component: NovaabaComponent },
  { path: 'livros', component: LivrosComponent },
  { path: 'login', component: LoginComponent },
  { path: 'design', component: DesignComponent},
  { path: 'footer', component: FooterComponent}
 ];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
