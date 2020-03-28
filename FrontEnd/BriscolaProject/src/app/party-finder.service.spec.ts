import { TestBed } from '@angular/core/testing';

import { PartyFinderService } from './party-finder.service';

describe('PartyFinderService', () => {
  let service: PartyFinderService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PartyFinderService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
