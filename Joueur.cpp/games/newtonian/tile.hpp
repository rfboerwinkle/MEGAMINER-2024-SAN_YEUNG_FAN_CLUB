#ifndef GAMES_NEWTONIAN_TILE_H
#define GAMES_NEWTONIAN_TILE_H

// Tile
// A Tile in the game that makes up the 2D map grid.

// DO NOT MODIFY THIS FILE
// Never try to directly create an instance of this class, or modify its member variables.
// Instead, you should only be reading its variables and calling its functions.

#include <vector>
#include <queue>
#include <deque>
#include <unordered_map>
#include <string>
#include <initializer_list>

#include "../../joueur/src/any.hpp"

#include "game_object.hpp"

#include "impl/newtonian_fwd.hpp"

// <<-- Creer-Merge: includes -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
// you can add additional #includes here
// <<-- /Creer-Merge: includes -->>

namespace cpp_client
{

namespace newtonian
{

/// <summary>
/// A Tile in the game that makes up the 2D map grid.
/// </summary>
class Tile_ : public Game_object_
{
public:

    /// <summary>
    /// The amount of blueium on this tile.
    /// </summary>
    const int& blueium;

    /// <summary>
    /// The amount of blueium ore on this tile.
    /// </summary>
    const int& blueium_ore;

    /// <summary>
    /// (Visualizer only) Different tile types, cracked, slightly dirty, etc. This has no effect on gameplay, but feel free to use it if you want.
    /// </summary>
    const int& decoration;

    /// <summary>
    /// The direction of a conveyor belt ('blank', 'north', 'east', 'south', or 'west'). Blank means conveyor doesn't move.
    /// </summary>
    const std::string& direction;

    /// <summary>
    /// Whether or not the tile is a wall.
    /// </summary>
    const bool& is_wall;

    /// <summary>
    /// The Machine on this Tile if present, otherwise null.
    /// </summary>
    const Machine& machine;

    /// <summary>
    /// The owner of this Tile, or null if owned by no-one. Only for generators and spawn areas.
    /// </summary>
    const Player& owner;

    /// <summary>
    /// The amount of redium on this tile.
    /// </summary>
    const int& redium;

    /// <summary>
    /// The amount of redium ore on this tile.
    /// </summary>
    const int& redium_ore;

    /// <summary>
    /// The Tile to the 'East' of this one (x+1, y). Null if out of bounds of the map.
    /// </summary>
    const Tile& tile_east;

    /// <summary>
    /// The Tile to the 'North' of this one (x, y-1). Null if out of bounds of the map.
    /// </summary>
    const Tile& tile_north;

    /// <summary>
    /// The Tile to the 'South' of this one (x, y+1). Null if out of bounds of the map.
    /// </summary>
    const Tile& tile_south;

    /// <summary>
    /// The Tile to the 'West' of this one (x-1, y). Null if out of bounds of the map.
    /// </summary>
    const Tile& tile_west;

    /// <summary>
    /// The type of Tile this is ('normal', 'generator', 'conveyor', or 'spawn').
    /// </summary>
    const std::string& type;

    /// <summary>
    /// The Unit on this Tile if present, otherwise null.
    /// </summary>
    const Unit& unit;

    /// <summary>
    /// The x (horizontal) position of this Tile.
    /// </summary>
    const int& x;

    /// <summary>
    /// The y (vertical) position of this Tile.
    /// </summary>
    const int& y;

    // <<-- Creer-Merge: member variables -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    // You can add additional member variables here. None of them will be tracked or updated by the server.
    // <<-- /Creer-Merge: member variables -->>


    /// <summary>
    /// The list of all valid directions Tiles can be in
    /// </summary>
    static const std::vector<std::string> directions;

    /// <summary>
    /// Gets the neighbors of this Tile
    /// </summary>
    /// <returns>The neighboring (adjacent) Tiles to this tile</returns>
    std::vector<Tile> get_neighbors();

    /// <summary>
    /// Checks if a Tile is pathable to units
    /// </summary>
    /// <returns>true if pathable, false otherwise</returns>
    bool is_pathable();

    /// <summary>
    /// Checks if this Tile has a specific neighboring Tile
    /// </summary>
    /// <param name="tile">Tile to check against</param>
    /// <returns>if the tile is a neighbor of this Tile, false otherwise</returns>
    bool has_neighbor(const Tile& tile);

   // <<-- Creer-Merge: methods -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
   // You can add additional methods here.
   // <<-- /Creer-Merge: methods -->>

   ~Tile_();

   // ####################
   // Don't edit these!
   // ####################
   /// \cond FALSE
   Tile_(std::initializer_list<std::pair<std::string, Any&&>> init);
   Tile_() : Tile_({}){}
   virtual void resize(const std::string& name, std::size_t size) override;
   virtual void change_vec_values(const std::string& name, std::vector<std::pair<std::size_t, Any>>& values) override;
   virtual void remove_key(const std::string& name, Any& key) override;
   virtual std::unique_ptr<Any> add_key_value(const std::string& name, Any& key, Any& value) override;
   virtual bool is_map(const std::string& name) override;
   virtual void rebind_by_name(Any* to_change, const std::string& member, std::shared_ptr<Base_object> ref) override;
    /// \endcond
    // ####################
    // Don't edit these!
    // ####################
};

} // newtonian

} // cpp_client

#endif // GAMES_NEWTONIAN_TILE_H
