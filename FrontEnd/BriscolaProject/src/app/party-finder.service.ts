import { Injectable } from '@angular/core';
import { HttpParams, HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { of } from 'rxjs';

const WIKI_URL = 'https://en.wikipedia.org/w/api.php';
const PARAMS = new HttpParams({
  fromObject: {
    action: 'opensearch',
    format: 'json',
    origin: '*'
  }
});

@Injectable()
export class WikipediaService {
  constructor(private http: HttpClient) { }

  search(term: string) {
    if (term === '') {
      return of([]);
    }

    return this.http
      .get(WIKI_URL, { params: PARAMS.set('search', term) }).pipe(
        map(response => response[1])
      );
  }
}