import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.scss'],
  imports: [FormsModule],
})
export class SearchBarComponent implements OnInit, OnDestroy {
  constructor(private router: Router, private route: ActivatedRoute) { }
  searchTerm: string = '';
  private subscription!: Subscription;

  ngOnInit() {
    this.subscription = this.route.queryParams.subscribe((params) => {
      if (this.router.url.startsWith('/search')) {
        this.searchTerm = params['q'] || '';
      }
    });
  }

  ngOnDestroy() {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }

  onSearch() {
    const queryParams: any = { q: this.searchTerm };
    const type = this.route.snapshot.queryParams['type'];
    if (type) {
      queryParams.type = type;
    }
    if (this.searchTerm.trim()) {
      this.router.navigate(['/search'], { queryParams });
    }
  }

  onKeyPress(event: KeyboardEvent) {
    if (event.key === 'Enter') {
      this.onSearch();
    }
  }
  onConfigPress() {
    this.router.navigate(['/config']);
  }

}
