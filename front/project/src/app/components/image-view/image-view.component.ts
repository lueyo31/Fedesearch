import { Component, OnInit, OnDestroy } from '@angular/core';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';
import { ActivatedRoute } from '@angular/router';
import { ModalService } from '../../services/modal/modal.service';
import { Result } from '../../models/result';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-image-view',
  templateUrl: './image-view.component.html',
  styleUrl: './image-view.component.scss',
})
export class ImageViewComponent implements OnInit, OnDestroy {
  result!: Result;
  isVisible = false;
  safeUrl!: SafeResourceUrl;
  type!: string;
  isVideoPlaying = false;
  private subscriptions: Subscription = new Subscription();

  constructor(
    private modalService: ModalService,
    private sanitizer: DomSanitizer,
    private route: ActivatedRoute
  ) { }

  ngOnInit() {
    this.subscriptions.add(
      this.route.queryParams.subscribe((params) => {
        this.type = params['type'];
      })
    );

    this.subscriptions.add(
      this.modalService.isModalOpen().subscribe((isVisible) => {
        this.isVisible = isVisible;
      })
    );

    this.subscriptions.add(
      this.modalService.getResult().subscribe((result: Result) => {
        this.result = result;
        this.isVideoPlaying = false; // Reset video playing state
        if (result.type.name === 'video' && result.type.embedUrl) {
          this.safeUrl = this.sanitizer.bypassSecurityTrustResourceUrl(result.type.embedUrl);
        }
      })
    );
  }

  ngOnDestroy() {
    this.subscriptions.unsubscribe();
  }

  playVideo() {
    this.isVideoPlaying = true;
  }

  closeDialog() {
    this.modalService.close();
    this.isVideoPlaying = false; // Reset video playing state
  }
}
