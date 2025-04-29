import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { PageService } from '../../services/page/page.service';
import { Page } from '../../models/page';
import { SearchBarComponent } from '../search-bar/search-bar.component';
import { ResultElementComponent } from '../result-element/result-element.component';
import { UpdateUrlBarComponent } from '../update-url-bar/update-url-bar.component';
import { TypeSelectorComponent } from '../type-selector/type-selector.component';
import { ImageViewComponent } from "../image-view/image-view.component";
import { LoadingAnimationComponent } from "../loading-animation/loading-animation.component";
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-results',
  imports: [
    SearchBarComponent,
    ResultElementComponent,
    UpdateUrlBarComponent,
    TypeSelectorComponent,
    RouterLink,
    ImageViewComponent,
    LoadingAnimationComponent
  ],
  templateUrl: './results.component.html',
  styleUrl: './results.component.scss',
})
export class ResultsComponent implements OnInit, OnDestroy {
  page!: Page;
  hasError = false; // Variable para rastrear errores
  isLoading = false; // Variable para rastrear el estado de carga
  q: string = ''; // Variable para almacenar la consulta de búsqueda
  type: string = 'web'; // Variable para almacenar el tipo de búsqueda
  pageNumber: number = 1; // Variable para almacenar el número de página actual
  private subscription!: Subscription;

  constructor(
    private pageService: PageService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  ngOnInit() {
    this.subscription = this.route.queryParams.subscribe((params) => {
      const q = params['q'];
      const page = params['page'] ? +params['page'] : 1;
      const type = params['type'] || 'web';
      this.q = q || ''; // Asignar la consulta de búsqueda
      this.pageNumber = page; // Asignar el número de página
      this.type = type; // Asignar el tipo de búsqueda

      if (q) {
        this.fetchData(q, page, type); // Llamar al nuevo método
      }
    });
  }

  ngOnDestroy() {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }

  changePage(currentPage: Page, num: number) {
    const newPage = currentPage.page + num;
    const q = this.q;
    const type = this.type;

    if (newPage > 0) {
      this.router.navigate(['/search'], {
        queryParams: { q, page: newPage, type },
      });
    }
  }


  private fetchData(query: string, page: number, type: string) {
    this.isLoading = true; // Iniciar el estado de carga
    this.pageService.search(query, page, type).subscribe({
      next: (page) => {
        this.page = page;
        this.hasError = false; // Reiniciar el estado de error
        this.isLoading = false; // Finalizar el estado de carga
        console.log(this.page);
      },
      error: (err) => {
        console.error('Search request failed', err);
        this.hasError = true; // Marcar que ocurrió un error
        this.isLoading = false; // Finalizar el estado de carga
      },
    });
  }
}
