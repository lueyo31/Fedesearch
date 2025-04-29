export interface Type {
  name: "web" | "image" | "video" | "new"; // generated in the queryparams type of user or type of search method
  thumbnail?: string; //URL map of thumbnail, only for image, video, new
  embedUrl?: string; //URL map of embedUrl, only for video

}
