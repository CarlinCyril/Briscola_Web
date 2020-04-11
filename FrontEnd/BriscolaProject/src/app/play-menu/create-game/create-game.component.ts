import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-create-game',
  templateUrl: './create-game.component.html',
  styleUrls: ['./create-game.component.scss']
})
export class CreateGameComponent implements OnInit {
  model = 1;

  constructor() { }

  @ViewChild('f') courseForm: NgForm;

  ngOnInit(): void {
  }

  onSubmit(form: NgForm) {
    console.log("Form submitted")
  }

  onDelete() {
  }

  ngOnDestroy() {    
  }

}
