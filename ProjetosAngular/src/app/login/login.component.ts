import {Component, OnInit} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {FormControl, FormGroup} from "@angular/forms";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent implements OnInit {
  form  = new FormGroup({
    email: new FormControl(''),
    password: new FormControl('')
  });

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }

  onSubmit(): void {
    this.http.post('http://localhost:8000/autenticacao/login/', this.form.value)
      .subscribe((response: any) => {
        // Login bem-sucedido, redirecionar para a página inicial
        console.log(response);
      });
  }
}
