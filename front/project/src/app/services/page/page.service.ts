import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Page } from '../../models/page';
import { HttpClient } from '@angular/common/http';
import { ConfigService } from '../config/config.service';

@Injectable({
  providedIn: 'root',
})
export class PageService {
  private apiUrl: string = '';
  constructor(private http: HttpClient, private configService: ConfigService) {
    this.configService.getApiUrl().subscribe((url) => {
      console.log('API URL updated in PageService:', url);
      this.apiUrl = url; // Update the API URL dynamically
    });
  }



  search(q: string, page: number = 1, type: string = 'web'): Observable<Page> {
    if (!this.apiUrl) {
      throw new Error('API URL is not configured.');
    }
    if (!q) {
      throw new Error('Query string cannot be empty.');
    }

    const url = `${this.apiUrl}/search`;
    const params = { q, page: page.toString(), category: type }; // Changed 'type' to 'category'
    return this.http.get<Page>(url, { params });
  }
  searchMock(
    q: string,
    page: number = 1,
    type: string = 'web'
  ): Observable<Page> {
    return this.http.get<Page>(
      `http://localhost:3000/data`
    );
  }
}
