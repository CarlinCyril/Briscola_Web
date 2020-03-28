import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BriscolaRuleComponent } from './briscola-rule.component';

describe('BriscolaRuleComponent', () => {
  let component: BriscolaRuleComponent;
  let fixture: ComponentFixture<BriscolaRuleComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BriscolaRuleComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BriscolaRuleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
