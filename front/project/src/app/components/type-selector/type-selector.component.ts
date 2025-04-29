import { Component, EventEmitter, OnDestroy, Output } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-type-selector',
  imports: [],
  templateUrl: './type-selector.component.html',
  styleUrl: './type-selector.component.scss',
})
export class TypeSelectorComponent implements OnDestroy {
  selectedType: string = 'web'; // Default type
  types: string[] = ['web', 'images', 'videos', 'news'];
  @Output() typeSelected: EventEmitter<string> = new EventEmitter<string>();
  private subscription!: Subscription;

  constructor(private router: Router, private route: ActivatedRoute) {
    this.subscription = this.route.queryParams.subscribe((params) => {
      this.selectedType = params['type'] || 'web';
    });
  }

  ngOnDestroy() {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }

  selectType(type: string) {
    this.selectedType = type;
    console.log('Selected type:', this.selectedType);
    this.router.navigate([], {
      queryParams: { type: this.selectedType },
      queryParamsHandling: 'merge',
    });
    this.typeSelected.emit(this.selectedType);
  }

  capitalizeFirstLetter(string: string): string {
    return string.charAt(0).toUpperCase() + string.slice(1);
  }
}
