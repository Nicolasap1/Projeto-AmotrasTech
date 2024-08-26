import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BookService {
  private apiUrl = 'http://localhost:8000/apiCadastro_Livro/';

  constructor(private http: HttpClient) {}

  getBooks(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  getBook(id: number): Observable<any> {
    return this.http.get<any[]>(`${this.apiUrl}${id}/`);
  }

  createBook(item: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, item);
  }

  updateBook(id: number, item: any): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}${id}/`, item);
  }

  deleteBook(id: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}${id}`);
  }
}
