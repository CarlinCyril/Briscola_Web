import { Component } from '@angular/core';
import {Observable, of} from 'rxjs';
import {catchError, debounceTime, distinctUntilChanged, tap, switchMap} from 'rxjs/operators';
import { WikipediaService } from '../services/party-finder.service';

@Component({
  selector: 'app-quick-search',
  templateUrl: './quick-search.component.html',
  providers: [WikipediaService],
  styleUrls: ['./quick-search.component.scss']
})

export class QuickSearchComponent {
  model: any;
  searching = false;
  searchFailed = false;

  constructor(private _service: WikipediaService) {}

  search = (text$: Observable<string>) =>
    text$.pipe(
      debounceTime(300),
      distinctUntilChanged(),
      tap(() => this.searching = true),
      switchMap(term =>
        this._service.search(term).pipe(
          tap(() => this.searchFailed = false),
          catchError(() => {
            this.searchFailed = true;
            return of([]);
          }))
      ),
      tap(() => this.searching = false)
    )
}