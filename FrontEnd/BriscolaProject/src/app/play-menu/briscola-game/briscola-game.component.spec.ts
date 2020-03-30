import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BriscolaGameComponent } from './briscola-game.component';

describe('BriscolaGameComponent', () => {
  let component: BriscolaGameComponent;
  let fixture: ComponentFixture<BriscolaGameComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BriscolaGameComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BriscolaGameComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
