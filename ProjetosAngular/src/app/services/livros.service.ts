import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CategoryService {
  private apiUrl = 'http://localhost:8000/apiCategoria/';

  constructor(private http: HttpClient) {}

  getCategories(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  getCategory(id: number): Observable<any> {
    return this.http.get<any[]>(`${this.apiUrl}${id}/`);
  }

  createCategory(item: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, item);
  }

  updateCategory(id: number, item: any): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}${id}/`, item);
  }

  deleteCategory(id: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}${id}`);
  }
}
