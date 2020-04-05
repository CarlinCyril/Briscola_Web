import { Injectable } from '@angular/core';
import { HttpParams, HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { of } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Game } from '../models/game';

const WIKI_URL = 'https://en.wikipedia.org/w/api.php';
const PARAMS = new HttpParams({
  fromObject: {
    action: 'opensearch',
    format: 'json',
    origin: '*'
  }
});

@Injectable()
export class GameFinderService {
  constructor(private http: HttpClient) { }

  private endpointUrl = environment.urlApi + '/Game'

  search(term: string) {
    if (term === '') {
      return of([]);
    }

    return this.http
      .get(this.endpointUrl, { params: PARAMS.set('search', term) }).pipe(
        map(response => response[1])
      );
  }

  getAll() {
    let result = this.http.get(this.endpointUrl);
    console.log(result);
    return result;
  }

  getGame(UUID: string) {
    let result = this.http.get(this.endpointUrl + '/' + UUID);
    console.log(result);
    return result;
  }

  createGame(game: Game) {
    return this.http.post(this.endpointUrl, game)
  }
}