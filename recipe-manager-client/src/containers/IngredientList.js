import React, { Component } from 'react'
import { connect } from "react-redux"
import { fetchIngredients, updateQueryString } from "../store/actions/ingredients"
import IngredientItem from "../components/IngredientItem"

class IngredientList extends Component {


    componentDidMount() {
        this.props.fetchIngredients(this.props.currentUser.user.user_id, this.props.queryString);
    }

    handleUpdate = (e) => {
        this.props.fetchIngredients(this.props.currentUser.user.user_id, e.target.value)
    }


    render() {
        const { ingredients } = this.props;
        let ingredientList = ingredients.map(ingredient => {
            return <IngredientItem
                key={ingredient.id}
                id={ingredient.id}
                user={ingredient.user}
                title={ingredient.title}
                article_number={ingredient.article_number}
                cost_per_unit={ingredient.cost_per_unit}
                unit_of_measure_amt={ingredient.unit_of_measure_amt}
                unit_of_measurement={ingredient.unit_of_measurement}
            />
        })
        return (
            <span className="col-sm-12">
                <label htmlFor='query'>Search Ingredient</label>
                <input
                    type="text"
                    className='form-control'
                    name="query"
                    id="query"
                    placeholder='E.g: Carrot'
                    value={this.props.queryString}
                    onChange={e => this.handleUpdate(e)}
                />
                <ul id='ingredients'>
                    {ingredientList}
                </ul>
            </span>
        )
    }
}

function mapStateToProps(state) {
    return {
        ingredients: state.ingredients,
        currentUser: state.currentUser,
        queryString: state.queryString
    }
}

export default connect(mapStateToProps, { fetchIngredients, updateQueryString })(IngredientList)