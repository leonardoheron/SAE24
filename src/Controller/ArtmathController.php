<?php

/**************************************************************
 * Site symfony : Art Mathématique - courbe de koch           *
 **************************************************************
 * (c) F. BONNARDOT, 28 Février 2022                          *
 * This code is given as is without warranty of any kind.     *
 * In no event shall the authors or copyright holder be liable*
 *    for any claim damages or other liability.               *
 **************************************************************/

namespace App\Controller;

// Inclus par défaut par Symfony
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

// Récupération des données d'un formulaire
use Symfony\Component\HttpFoundation\Request;

// Exécution d'un process (ici fonction python)
// Doc : https://symfony.com/doc/current/components/process.html
use Symfony\Component\Process\Exception\ProcessFailedException;
use Symfony\Component\Process\Process;

// Pour renvoyer un fichier directement
use Symfony\Component\HttpFoundation\File\File;


class ArtmathController extends AbstractController
{
    /**
     * @Route("/", name="racine")
     */
    public function racine() : Response
    {
        // Redirige vers /artmath si on va sur le site sans
        //  indiquer le nom de la route
        return $this->render('artmath/home.html.twig');
    }

    /**
     * @Route("/artmath", name="app_artmath")
     */
    public function index(): Response
    {
        return $this->render('artmath/index.html.twig', [
            'fichier' => '',
        ]);
    }
    /**
     * @Route("/fig2", name="app_fig2")
     */
    public function fig2(): Response
    {
        return $this->render('artmath/fig2.html.twig', [
            'fichier_nees' => '',
        ]);
    }
    /**
     * @Route("/fig3", name="app_fig3")
     */
    public function fig3(): Response
    {
        return $this->render('artmath/carre_latin.html.twig', [
            'oeuvre' => '',
        ]);
    }


    /**
     * @Route("/calculer", name="calculer")
     */
    public function calculer(Request $request): Response
    {
        // Récupère les paramètres issus du formulaire (on indique le champ name)
        $dimension = $request -> request -> get("dimension") ;
        // Pour les boutons : si appui contenu champ value sinon NULL
        $calculer  = $request -> request -> get("calculer");
        $imprimer  = $request -> request -> get("imprimer");
        // Oui : Appelle le script Python koch.py qui se trouve dans le répertoire /public
        $process = new Process(['python3','koch.py',$dimension]);
        $process -> run();
        // Récupère la valeur de retour renvoyé par le script python
        $fichier=$process->getOutput();

        // Retourne un message si l'éxécution c'est mal passée
        if (!$process->isSuccessful())
            return new Response ("Erreur lors de l'éxécution du script Python :<br>".$process->getErrorOutput());    

        // A t'on appuyé sur calculer ?
        if ($calculer!=NULL)
            return $this->render('artmath/index.html.twig', [
                'fichier' => $fichier,
            ]);
        else {
            // On a appuyé sur imprimer
            return $this->render('artmath/imprimer.html.twig', [
                'fichier' => $fichier,
            ]);
        }
    }
    /**
     * @Route("/calculer_nees", name="calculer_nees")
     */
    public function calculer_nees(Request $request): Response
    {
        // Récupère les paramètres issus du formulaire (on indique le champ name)
        $dimension_ama = $request -> request -> get("dimension_ama") ;
        $dimension_amr = $request -> request -> get("dimension_amr") ;
        $dimension_nbc = $request -> request -> get("dimension_nbc") ;
        $dimension_nbl = $request -> request -> get("dimension_nbl") ;
        // Pour les boutons : si appui contenu champ value sinon NULL
        $calculer_nees  = $request -> request -> get("calculer_nees");
        $imprimer_nees  = $request -> request -> get("imprimer_nees");


        // Oui : Appelle le script Python koch.py qui se trouve dans le répertoire /public
        $process_nees = new Process(['python3',"nees_carre.py",$dimension_ama,$dimension_amr,$dimension_nbc,$dimension_nbl]);
        $process_nees -> run();
        // Récupère la valeur de retour renvoyé par le script python
        $fichier_nees="reponse.png";

        // Retourne un message si l'éxécution c'est mal passée
        if (!$process_nees->isSuccessful())
            return new Response ("Erreur lors de l'éxécution du script Python :<br>".$process_nees->getErrorOutput());    

        // A t'on appuyé sur calculer ?
        if ($calculer_nees!=NULL)
            return $this->render('artmath/fig2.html.twig', [
                'fichier_nees' => $fichier_nees,
            ]);
        else {
            // On a appuyé sur imprimer
            return $this->render('artmath/imprimer_nees.html.twig', [
                'fichier_nees' => $fichier_nees,
            ]);
        }
    }
    /**
     * @Route("/carre_latin", name="calculer_nees")
     */
    public function carre_latin(Request $request): Response
    {
        // Pour les boutons : si appui contenu champ value sinon NULL
        $oeuvre  = $_POST['carre_latin'];


        // Oui : Appelle le script Python koch.py qui se trouve dans le répertoire /public
        $process_carre_latin = new Process(['python3',"carre_latin.py"]);
        $process_carre_latin -> run();
        // Récupère la valeur de retour renvoyé par le script python
        $fichier_nees="reponse.png";

        // Retourne un message si l'éxécution c'est mal passée
        if (!$process_carre_latin->isSuccessful())
            return new Response ("Erreur lors de l'éxécution du script Python :<br>".$process_carre_latin->getErrorOutput());    

        // A t'on appuyé sur calculer ?
        if ($oeuvre!=NULL)
            return $this->render('artmath/carre_latin.html.twig', [
                'oeuvre' => $fichier_nees,
            ]);
        else {
            // On a appuyé sur imprimer
            return $this->render('artmath/carre_latin.html.twig', [
                'oeuvre' => $fichier_nees,
            ]);
        }
    }
}
