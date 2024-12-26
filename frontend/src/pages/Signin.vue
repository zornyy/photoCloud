<template>
    <ion-page>
      <ion-header>
        <ion-toolbar>
          <ion-title>Sign In</ion-title>
        </ion-toolbar>
      </ion-header>
  
      <ion-content class="ion-padding">
        <ion-card>
          <ion-card-header>
            <ion-card-title>First time here ?</ion-card-title>
          </ion-card-header>
          <ion-card-content>
            <ion-item>
                <ion-input label-placement="stacked" label="Email" type="email" placeholder="me@example.com"/>
            </ion-item>
            <ion-item>
                <ion-input label-placement="stacked" label="Username" placeholder="Obi-Wan"/>
            </ion-item>
            <ion-item>
                <ion-input label-placement="stacked" label="Password" type="password" placeholder="MyPassword"/>
            </ion-item>
            <ion-item>
                <ion-input label-placement="stacked" label="Confirm Password" type="password" placeholder="MyPassword"/>
            </ion-item>
            <ion-button expand="block">Sign In</ion-button>
          </ion-card-content>
        </ion-card>
      </ion-content>
    </ion-page>
  </template>
  
  <script>
  import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonCard, IonCardHeader, IonCardTitle, IonCardContent, IonItem, IonLabel, IonInput, IonButton } from '@ionic/vue';
  
  export default {
    name: 'Login',
    components: {
      IonPage,
      IonHeader,
      IonToolbar,
      IonTitle,
      IonContent,
      IonCard,
      IonCardHeader,
      IonCardTitle,
      IonCardContent,
      IonItem,
      IonLabel,
      IonInput,
      IonButton
    },

    // LOGIC
  };


</script>

<style scoped>
  ion-card {
    margin-top: 20px;
  }
</style>
  