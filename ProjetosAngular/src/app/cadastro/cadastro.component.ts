import {Component, OnInit} from '@angular/core';
import {FormControl, FormGroup} from "@angular/forms";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.component.html',
  styleUrl: './cadastro.component.css'
})
export class CadastroComponent implements OnInit {
  form = new FormGroup({
    nome: new FormControl(''),
    email: new FormControl(''),
    password: new FormControl(''),
  });

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }

  onSubmit(): void {
    this.http.post('http://127.0.0.1:8000/apiCadastro_Usuario/', this.form.value)
      .subscribe((response: any) => {
        // Registro bem-sucedido, redirecionar para a página de login
        console.log(response);
      });
  }
}
