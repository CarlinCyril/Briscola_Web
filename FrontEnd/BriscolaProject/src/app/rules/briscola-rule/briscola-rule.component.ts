import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-briscola-rule',
  templateUrl: './briscola-rule.component.html',
  styleUrls: ['./briscola-rule.component.scss']
})
export class BriscolaRuleComponent implements OnInit {

  active = 1;

  constructor() { }

  ngOnInit(): void {
  }

}
