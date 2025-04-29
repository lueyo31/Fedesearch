import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Result } from '../../models/result';

import { ModalService } from '../../services/modal/modal.service';
import { LoadingAnimationComponent } from "../loading-animation/loading-animation.component";

@Component({
  selector: 'app-result-element',
  imports: [LoadingAnimationComponent],
  templateUrl: './result-element.component.html',
  styleUrl: './result-element.component.scss',
})
export class ResultElementComponent {
  @Input() result!: Result;
  //@Output() imageViewed = new EventEmitter<Result>();
  //@Output() videoViewed = new EventEmitter<Result>();


  constructor(private modalService: ModalService) {}

  getFaviconUrl(url: string): string {
    return `https://www.google.com/s2/favicons?domain=${url}`;
  }

  openImageDialog() {
    this.modalService.open(this.result);
  }
  openVideoDialog() {
    this.modalService.open(this.result);
  }
}
