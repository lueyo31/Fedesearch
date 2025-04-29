import { Component } from '@angular/core';
import { SearchBarComponent } from '../search-bar/search-bar.component';

@Component({
  selector: 'app-inicio',
  imports: [SearchBarComponent],
  templateUrl: './inicio.component.html',
  styleUrls: ['./inicio.component.scss'], // Corrected to use SCSS file
})
export class InicioComponent {}
