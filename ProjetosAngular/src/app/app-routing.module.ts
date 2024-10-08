import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {LoginComponent} from "./login/login.component";
import {DesignComponent} from "./design/design.component";
import {FooterComponent} from "./footer/footer.component";
import {CadastroComponent} from "./cadastro/cadastro.component";
import {ViewComponent} from "./view/view.component";


const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'design', component: DesignComponent},
  { path: 'footer', component: FooterComponent},
  { path: 'cadastro', component: CadastroComponent},
  {path:'view', component: ViewComponent},
 ];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
