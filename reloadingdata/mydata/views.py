from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404

from .models import Gun, Bullet
from .forms import GunForm, BulletForm


class HomeView(ListView):
    model = Gun
    template_name = "home.html"


class GunsView(ListView):
    model = Gun
    template_name = "guns.html"


@login_required
def gunview(request, gun_id):
    """Show a single gun and all its info."""
    #guns = Gun.objects.filter(owner=request.user, id=gun_id).prefetch_related('bullets__results__velocity')
    gun = Gun.objects.get(pk=gun_id)
    # Make sure the gun belongs to the current user.
    
    if gun.owner != request.user:
        raise Http404
    
    context = {'gun': gun}  
    return render(request, 'gun.html', context)

@login_required
def AddGun(request):
    """Add a new gun."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = GunForm()
    else:
        # POST data submitted; process data.
        form = GunForm(request.POST)
        if form.is_valid():
            new_gun = form.save(commit=False)
            new_gun.owner = request.user
            form.save()
            return HttpResponseRedirect(reverse('guns'))
    context = {'form': form}
    return render(request, 'add_gun.html', context)

@login_required
def addbullet(request, gun_id):
    """Add a new bullet."""
    gun = Gun.objects.get(id=gun_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BulletForm()
    else:
        # POST data submitted; process data.
        form = BulletForm(data=request.POST)
        if form.is_valid():
            new_bullet = form.save(commit=False)
            new_bullet.gun = gun
            new_bullet.save()
            return HttpResponseRedirect(reverse('gun', args=[gun_id]))
    context = {'form': form,'gun':gun}
    return render(request, 'add_bullet.html', context)

@login_required
def edit_bullet(request, bullet_id):
    """Edit an existing result."""
    bullet = Bullet.objects.get(id=bullet_id)
    gun = bullet.gun
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = BulletForm(instance=bullet)
    else:
        # POST data submitted; process data.
        form = BulletForm(instance=bullet, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('gun', args=[gun.id]))
    context = {'bullet': bullet, 'gun': gun, 'form': form}
    return render(request, 'edit_bullet.html', context)

@login_required
def delete_bullet(request, bullet_id):
    """delete an existing result."""
    bullet = Bullet.objects.get(id=bullet_id)
    bullet.delete()
    gun = bullet.gun
    return HttpResponseRedirect(reverse('gun', args=[gun.id]))

@login_required
def view_graph(request, bullet_id):
    """Show a single bullet graph."""
    
    bullet = Bullet.objects.filter(id=bullet_id).prefetch_related('results__velocity')
    velocitylist = []
    chargelist = []
    moalist = []
    for b in bullet: 
        gun = b.gun
        for result in b.results.all():
            chargelist.append(result.charge)
            moalist.append(result.moa)
            total_avg = 0  
            for velocity in result.velocity.all():
                total_avg += velocity.velocity
            total_avg /= 3
            velocitylist.append(total_avg) 

    #send no data for velocitylist if the values are 0
    if velocitylist[0] == 0:
        velocitylist.clear() 
                             
    context = {'gun': gun, 'bullet': bullet, 'velocitylist': velocitylist, 'chargelist':chargelist, 'moalist':moalist} 
    return render(request, 'graph.html', context)
