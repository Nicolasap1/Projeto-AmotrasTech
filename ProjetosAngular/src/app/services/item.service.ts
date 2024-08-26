import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private apiUrl = 'http://localhost:8000/apiCadastro_Usuario/';

  constructor(private http: HttpClient) { }

  getUsers(): Observable<any[]> {
   return this.http.get<any[]>(this.apiUrl);
  }

  getUser(id: number): Observable<any> {
   return this.http.get<any[]>(`${this.apiUrl}${id}/`);
  }
  createUser(item: any): Observable<any>{
   return this.http.post<any>(this.apiUrl, item);
  }

  updateUser(id:number, item: any): Observable<any>{
   return this.http.put<any>(`${this.apiUrl}${id}/`,item);
  }

  deleteUser(id: number): Observable<any>{
   return this.http.delete<any>(`${this.apiUrl}${id}`);
  }
}

